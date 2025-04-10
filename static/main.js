async function fetchData() {
  const res = await fetch("/api/status");
  const data = await res.json();
  return data;
}

const cpuData = [];
const memData = [];
const labels = [];

const ctx = document.getElementById("myChart").getContext("2d");
const chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "CPU使用率（%）",
        data: cpuData,
        borderWidth: 1
      },
      {
        label: "メモリ使用率（%）",
        data: memData,
        borderWidth: 1
      }
    ]
  },
  options: {
    animation: false,
    scales: {
      y: {
        beginAtZero: true,
        max: 100
      }
    }
  }
});

setInterval(async () => {
  const now = new Date().toLocaleTimeString();
  const data = await fetchData();
  labels.push(now);
  cpuData.push(data.cpu);
  memData.push(data.mem);

  if (labels.length > 10) {
    labels.shift();
    cpuData.shift();
    memData.shift();
  }

  chart.update();
}, 5000);