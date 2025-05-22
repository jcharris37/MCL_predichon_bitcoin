const ctx = document.getElementById('predictionChart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Precio Predicho',
      data: [],
      borderColor: 'rgb(75, 192, 192)',
      backgroundColor: 'rgba(75, 192, 192, 0.1)',
      tension: 0.3,
      fill: true,
      pointBackgroundColor: 'rgb(75, 192, 192)',
      pointRadius: 5
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: true,
        position: 'top'
      },
      tooltip: {
        mode: 'index',
        intersect: false
      },
      title: {
        display: true,
        text: 'Historial de Predicciones de Precio Bitcoin',
        font: {
          size: 16
        }
      }
    },
    interaction: {
      mode: 'nearest',
      axis: 'x',
      intersect: false
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Número de Predicción'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Precio (normalizado)'
        },
        beginAtZero: true
      }
    }
  }
});

document.getElementById('predictionForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const jsonData = {};

  formData.forEach((value, key) => {
    jsonData[key] = parseFloat(value);
  });

  const response = await fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonData)
  });

  const result = await response.json();

  if (response.ok) {
    const predicted = result.predicted_price.toFixed(4);
    document.getElementById('result').innerHTML = `✅ Precio Predicho: <strong>${predicted}</strong>`;
    
    const index = chart.data.labels.length + 1;
    chart.data.labels.push('Predicción ' + index);
    chart.data.datasets[0].data.push(predicted);
    chart.update();
  } else {
    document.getElementById('result').innerHTML = `❌ Error: ${result.error}`;
  }
});
