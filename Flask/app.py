"""
EcoAudit - Regulatory Technology Compliance Dashboard
A Flask-based institutional compliance and verification system.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Helper function to load JSON data
def load_json(filename):
    """Load JSON data from the data directory."""
    data_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def index():
    """Redirect to DTU dashboard."""
    return render_template('index.html')


@app.route('/institution/dtu')
def dtu_dashboard():
    """
    DTU Institutional Compliance Dashboard.
    Primary dashboard showing verification pipeline, events, and compliance metrics.
    """
    events = load_json('dtu_events.json')
    metrics = load_json('dtu_metrics.json')
    
    # Calculate KPIs
    total_logged = len(events['events'])
    verified_count = sum(1 for e in events['events'] if e['status'] == 'Verified')
    partially_verified = sum(1 for e in events['events'] if e['status'] == 'Partially Verified')
    pending_count = sum(1 for e in events['events'] if e['status'] == 'Pending')
    flagged_count = sum(1 for e in events['events'] if e['status'] == 'Flagged')
    under_verification = partially_verified + pending_count
    
    trust_score = (verified_count / total_logged * 100) if total_logged > 0 else 0
    
    kpis = {
        'trust_score': round(trust_score, 1),
        'verified_count': verified_count,
        'total_logged': total_logged,
        'community_wealth': metrics['summary']['community_wealth'],
        'landfill_gap': metrics['summary']['landfill_gap'],
        'audit_readiness': metrics['summary']['audit_readiness']
    }
    
    pipeline = {
        'logged': total_logged,
        'under_verification': under_verification,
        'verified': verified_count,
        'flagged': flagged_count
    }
    
    return render_template(
        'dtu_dashboard.html',
        kpis=kpis,
        pipeline=pipeline,
        events=events['events'],
        metrics=metrics,
        compliance_matrix=metrics['compliance_matrix']
    )


@app.route('/public/benchmark')
def public_benchmark():
    """
    Public National Benchmark Dashboard.
    Read-only, aggregated comparison of institutions.
    """
    benchmark_data = load_json('public_benchmark.json')
    
    return render_template(
        'public_dashboard.html',
        institutions=benchmark_data['institutions'],
        last_updated=benchmark_data['last_updated']
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
