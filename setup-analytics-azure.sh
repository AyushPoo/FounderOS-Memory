#!/bin/bash
set -e
BASE=/home/ayush/analytics
mkdir -p $BASE/backups

cat > $BASE/package.json << 'EOF'
{"name":"analytics-api","version":"1.0.0","main":"server.js","scripts":{"start":"node server.js"},"dependencies":{"better-sqlite3":"^9.4.3","cookie-parser":"^1.4.6","cors":"^2.8.5","dotenv":"^16.4.5","express":"^4.18.3"}}
EOF

printf 'DASHBOARD_PASSWORD=FS$123\nPORT=3001\nDB_PATH=/home/ayush/analytics/metrics.db\nINTERNAL_API_KEY=fs_internal_k9x2mQ7pLw4nRt8vYz3bJc6hD1eA5sUo\n' > $BASE/.env

cat > $BASE/product-config.json << 'EOF'
{"fs001-saas-financial-model":{"name":"SaaS Financial Model","category":"SaaS","type":"excel"},"fs002-advanced-b2b-saas":{"name":"Advanced B2B SaaS","category":"SaaS","type":"excel"},"fs003-marketplace-model":{"name":"Marketplace Model","category":"Marketplace","type":"excel"},"fs004-d2c-model":{"name":"D2C Model","category":"D2C","type":"excel"},"pomodoro-timer":{"name":"Pomodoro Timer","category":"Free Tool","type":"web_app"},"startup-cost-calculator":{"name":"Startup Cost Calculator","category":"Free Tool","type":"web_app"}}
EOF

cat > $BASE/server.js << 'SERVEREOF'
require('dotenv').config();
const express=require('express'),cookieParser=require('cookie-parser'),cors=require('cors'),crypto=require('crypto'),Database=require('better-sqlite3');
const app=express(),PORT=process.env.PORT||3001,DB_PATH=process.env.DB_PATH,PW=process.env.DASHBOARD_PASSWORD,IK=process.env.INTERNAL_API_KEY,SC='fs_analytics_session';
app.use(express.json());app.use(cookieParser());
app.use(cors({origin:['http://localhost:5173','https://analytics.foundersystems.in','https://foundersystems-analytics.vercel.app'],credentials:true}));
let db;
function initDb(){db=new Database(DB_PATH);db.exec(`CREATE TABLE IF NOT EXISTS daily_metrics(id INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT NOT NULL,product_slug TEXT NOT NULL,platform TEXT NOT NULL,revenue REAL DEFAULT 0,sales_count INTEGER DEFAULT 0,refund_count INTEGER DEFAULT 0,page_views INTEGER DEFAULT 0,unique_visitors INTEGER DEFAULT 0,bounce_rate REAL DEFAULT 0,avg_session_duration REAL DEFAULT 0,created_at TEXT DEFAULT CURRENT_TIMESTAMP);CREATE TABLE IF NOT EXISTS weekly_insights(id INTEGER PRIMARY KEY AUTOINCREMENT,week_start TEXT NOT NULL,category TEXT NOT NULL,total_revenue REAL DEFAULT 0,total_sales INTEGER DEFAULT 0,avg_conversion_rate REAL DEFAULT 0,top_product TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);`);}
const h=s=>crypto.createHash('sha256').update(s).digest('hex');
function auth(req,res,next){if(req.headers['x-internal-key']===IK)return next();const t=req.cookies[SC];if(t&&t===h(PW+'_session'))return next();res.status(401).json({error:'Unauthorized'});}
app.post('/api/auth',(req,res)=>{if(!req.body.password||req.body.password!==PW)return res.status(401).json({error:'Invalid password'});res.cookie(SC,h(PW+'_session'),{httpOnly:true,maxAge:86400000});res.json({success:true});});
app.post('/api/logout',(req,res)=>{res.clearCookie(SC);res.json({success:true});});
app.post('/api/ingest',(req,res)=>{const{date,product_slug,platform,revenue,sales_count,refund_count,page_views,unique_visitors,bounce_rate,avg_session_duration}=req.body;if(!date||!product_slug||!platform)return res.status(400).json({error:'Missing fields'});db.prepare('DELETE FROM daily_metrics WHERE date=? AND product_slug=? AND platform=?').run(date,product_slug,platform);db.prepare('INSERT INTO daily_metrics(date,product_slug,platform,revenue,sales_count,refund_count,page_views,unique_visitors,bounce_rate,avg_session_duration)VALUES(?,?,?,?,?,?,?,?,?,?)').run(date,product_slug,platform,revenue||0,sales_count||0,refund_count||0,page_views||0,unique_visitors||0,bounce_rate||0,avg_session_duration||0);res.json({success:true});});
app.post('/api/ingest/insight',(req,res)=>{const{week_start,category,total_revenue,total_sales,avg_conversion_rate,top_product}=req.body;if(!week_start||!category)return res.status(400).json({error:'Missing fields'});db.prepare('DELETE FROM weekly_insights WHERE week_start=? AND category=?').run(week_start,category);db.prepare('INSERT INTO weekly_insights(week_start,category,total_revenue,total_sales,avg_conversion_rate,top_product)VALUES(?,?,?,?,?,?)').run(week_start,category,total_revenue||0,total_sales||0,avg_conversion_rate||0,top_product||null);res.json({success:true});});
app.get('/api/overview',auth,(req,res)=>{const{start,end}=req.query;if(!start||!end)return res.status(400).json({error:'required'});const c=db.prepare('SELECT SUM(revenue) as r,SUM(sales_count) as s,SUM(unique_visitors) as v FROM daily_metrics WHERE date>=? AND date<=?').get(start,end);const days=Math.ceil((new Date(end)-new Date(start))/86400000);const ps=new Date(start);ps.setDate(ps.getDate()-days-1);const pe=new Date(start);pe.setDate(pe.getDate()-1);const p=db.prepare('SELECT SUM(revenue) as r,SUM(sales_count) as s,SUM(unique_visitors) as v FROM daily_metrics WHERE date>=? AND date<=?').get(ps.toISOString().split('T')[0],pe.toISOString().split('T')[0]);const best=db.prepare('SELECT product_slug,SUM(revenue) as rev FROM daily_metrics WHERE date>=? AND date<=? GROUP BY product_slug ORDER BY rev DESC LIMIT 1').get(start,end);const pct=(a,b)=>b>0?Math.round(((a-b)/b)*100):null;res.json({total_revenue:c.r||0,total_sales:c.s||0,total_visitors:c.v||0,best_product:best?{slug:best.product_slug,revenue:best.rev}:null,changes:{revenue_pct:pct(c.r||0,p.r||0),sales_pct:pct(c.s||0,p.s||0),visitors_pct:pct(c.v||0,p.v||0)}});});
app.get('/api/metrics',auth,(req,res)=>{const{start,end,product}=req.query;if(!start||!end)return res.status(400).json({error:'required'});let q='SELECT product_slug,SUM(revenue) as revenue,SUM(sales_count) as sales_count,SUM(refund_count) as refund_count,SUM(page_views) as page_views,SUM(unique_visitors) as unique_visitors FROM daily_metrics WHERE date>=? AND date<=?';const p=[start,end];if(product){q+=' AND product_slug=?';p.push(product);}q+=' GROUP BY product_slug ORDER BY revenue DESC';const rows=db.prepare(q).all(...p);const days=Math.ceil((new Date(end)-new Date(start))/86400000);const ps=new Date(start);ps.setDate(ps.getDate()-days-1);const pe=new Date(start);pe.setDate(pe.getDate()-1);const pr=db.prepare(q).all(ps.toISOString().split('T')[0],pe.toISOString().split('T')[0],...(product?[product]:[]));const pm={};pr.forEach(r=>pm[r.product_slug]=r);const pct=(a,b)=>b>0?Math.round(((a-b)/b)*100):null;res.json(rows.map(r=>({...r,conversion_rate:r.page_views>0?(r.sales_count/r.page_views*100).toFixed(2):'0.00',revenue_change_pct:pct(r.revenue,pm[r.product_slug]?.revenue||0),visitors_change_pct:pct(r.unique_visitors,pm[r.product_slug]?.unique_visitors||0)})));});
app.get('/api/trends',auth,(req,res)=>{const{start,end,product}=req.query;if(!start||!end)return res.status(400).json({error:'required'});let q='SELECT date,product_slug,SUM(revenue) as revenue,SUM(unique_visitors) as unique_visitors FROM daily_metrics WHERE date>=? AND date<=?';const p=[start,end];if(product){q+=' AND product_slug=?';p.push(product);}q+=' GROUP BY date,product_slug ORDER BY date ASC';res.json(db.prepare(q).all(...p));});
app.get('/api/insights',auth,(req,res)=>{res.json(db.prepare('SELECT * FROM weekly_insights ORDER BY week_start DESC LIMIT 20').all());});
initDb();app.listen(PORT,'0.0.0.0',()=>console.log('Analytics API on port '+PORT));
SERVEREOF

cd $BASE && npm install --production 2>&1 | tail -2
pm2 delete analytics-api 2>/dev/null || true
pm2 start $BASE/server.js --name analytics-api
pm2 save
sleep 2
curl -s -X POST http://localhost:3001/api/auth -H 'Content-Type: application/json' -d '{"password":"FS$123"}'
echo -e "\n=== Done ==="
