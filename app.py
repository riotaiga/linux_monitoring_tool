from flask import Flask, render_template
import linux_monitoring_tool.monitoring as monitoring

app = Flask(__name__)
 
@app.route('/')
def index(): 
    mertrics = monitoring.get_system_metrics()
    return render_template('dashboard.html', metrics=metrics) 

if __name__ == '__main__':
    app.run(debug=True)
    