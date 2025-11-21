import PropTypes from 'prop-types';
import classNames from 'classnames';

const severityMap = {
  info: 'soft-blue',
  warning: 'soft-yellow',
  critical: 'soft-red'
};

export default function Alerts({ alerts }) {
  return (
    <div className="panel alerts-panel">
      <header className="panel-header">
        <p>Alert Center</p>
        <span>{alerts.length} active</span>
      </header>
      <div className="alert-list">
        {alerts.slice(0, 6).map((alert) => (
          <article key={alert.id} className={classNames('alert-item', severityMap[alert.severity])}>
            <div>
              <p>{alert.title}</p>
              <small>{alert.description}</small>
            </div>
            <span>{alert.timestamp}</span>
          </article>
        ))}
        {alerts.length === 0 && <p className="muted">No alerts triggered</p>}
      </div>
    </div>
  );
}

Alerts.propTypes = {
  alerts: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      severity: PropTypes.oneOf(['info', 'warning', 'critical']).isRequired,
      timestamp: PropTypes.string.isRequired
    })
  ).isRequired
};

