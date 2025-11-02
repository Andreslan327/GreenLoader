document.addEventListener('DOMContentLoaded', () => {
  const output = document.getElementById('output');
  const urlInput = document.getElementById('urlInput');
  const qualitySelect = document.getElementById('qualitySelect');

  // Botones de descarga
  document.getElementById('audioBtn').addEventListener('click', () => handleDownload('audio'));
  document.getElementById('videoBtn').addEventListener('click', () => handleDownload('video'));

  // Botones externos (GitHub y Reporte)
  const starBtn = document.getElementById('starGithubBtn');
  const reportBtn = document.getElementById('reportIssueBtn');

  if (starBtn) {
    starBtn.addEventListener('click', () => {
      console.log('Click en Estrella en GitHub');
      window.electronAPI.openExternalLink('https://github.com/Andreslan327/GreenLoader/tree/main');
    });
  }

  if (reportBtn) {
    reportBtn.addEventListener('click', () => {
      console.log('Click en Reportar un problema');
      window.electronAPI.openExternalLink('https://github.com/Andreslan327/GreenLoader/discussions/new?category=reportes');
    });
  }

  // Mostrar mensajes de éxito y error en descarga
  window.electronAPI.onDownloadSuccess((event, data) => {
    output.textContent = `✅ ${data.message}`;
  });

  window.electronAPI.onDownloadError((event, data) => {
    output.textContent = `❌ ${data.error}`;
  });

  // Función para iniciar descarga
  function handleDownload(type) {
    const url = urlInput.value.trim();
    const quality = qualitySelect.value;
    if (!url) {
      output.textContent = '⚠️ Por favor ingresa un link válido.';
      urlInput.focus();
      return;
    }

    output.textContent = '⏳ Descargando...';

    window.electronAPI.downloadMedia({ type, url, quality });
  }
});
