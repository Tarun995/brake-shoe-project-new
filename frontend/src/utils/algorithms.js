export const calculateQualityScore = (snapshot) => {
  const tempPenalty = Math.max(0, snapshot.temperature - 210) * 0.8;
  const pressurePenalty = Math.max(0, snapshot.pressure - 115) * 0.9;
  const vibrationPenalty = snapshot.vibration * 1.5;
  const baseScore = 100 - tempPenalty - pressurePenalty - vibrationPenalty;
  return Math.max(50, Math.min(100, baseScore));
};

export const calculateDefectProbability = (snapshot, qualityScore) => {
  const stressFactor =
    (Math.max(0, snapshot.temperature - 205) +
      Math.max(0, snapshot.pressure - 110) +
      snapshot.vibration * 2) /
    300;
  const qualityFactor = (100 - qualityScore) / 150;
  return Math.min(0.9, Math.max(0.01, stressFactor + qualityFactor));
};

export const deriveBatchDelta = (snapshot) => {
  const throughput = Math.max(1, Math.round(60 / snapshot.cycleTime));
  return throughput;
};

