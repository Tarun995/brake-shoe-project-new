import PropTypes from 'prop-types';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Legend
} from 'recharts';

export default function RealtimeCharts({ data }) {
  return (
    <div className="panel">
      <header className="panel-header">
        <p>Real-time Telemetry</p>
        <span>Last {data.length} cycles</span>
      </header>
      <div className="chart-wrapper">
        <ResponsiveContainer width="100%" height={320}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1f2937" />
            <XAxis dataKey="timestamp" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip
              contentStyle={{ background: '#0b1220', border: '1px solid #1f2937' }}
              labelStyle={{ color: '#e2e8f0' }}
            />
            <Legend />
            <Line type="monotone" dataKey="temperature" stroke="#fb7185" dot={false} strokeWidth={2} />
            <Line type="monotone" dataKey="pressure" stroke="#38bdf8" dot={false} strokeWidth={2} />
            <Line type="monotone" dataKey="cycleTime" stroke="#a5b4fc" dot={false} strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

RealtimeCharts.propTypes = {
  data: PropTypes.arrayOf(
    PropTypes.shape({
      timestamp: PropTypes.string.isRequired,
      temperature: PropTypes.number.isRequired,
      pressure: PropTypes.number.isRequired,
      cycleTime: PropTypes.number.isRequired
    })
  ).isRequired
};

