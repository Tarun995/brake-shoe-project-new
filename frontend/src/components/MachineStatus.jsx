import PropTypes from 'prop-types';

export default function MachineStatus({ data }) {
  const pillClass = `status-${data.state.replace(/\s+/g, '-').toLowerCase()}`;
  return (
    <div className="panel">
      <header className="panel-header">
        <p>Machine Status</p>
        <span className={`status-pill ${pillClass}`}>
          {data.state}
        </span>
      </header>
      <div className="panel-body">
        <div className="status-row">
          <p>Throughput</p>
          <strong>{data.throughput} units/hr</strong>
        </div>
        <div className="status-row">
          <p>Load Balance</p>
          <strong>{data.loadBalance}%</strong>
        </div>
        <div className="status-row">
          <p>Energy Usage</p>
          <strong>{data.energyUsage} kWh</strong>
        </div>
        <div className="status-row">
          <p>CPU Utilization</p>
          <strong>{data.cpuUtilization}%</strong>
        </div>
        <p className="status-note">{data.note}</p>
      </div>
    </div>
  );
}

MachineStatus.propTypes = {
  data: PropTypes.shape({
    state: PropTypes.string.isRequired,
    throughput: PropTypes.number.isRequired,
    loadBalance: PropTypes.number.isRequired,
    energyUsage: PropTypes.number.isRequired,
    cpuUtilization: PropTypes.number.isRequired,
    note: PropTypes.string.isRequired
  }).isRequired
};

