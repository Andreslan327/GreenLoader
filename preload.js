const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  downloadMedia: (args) => ipcRenderer.send('download-media', args),
  onDownloadSuccess: (callback) => ipcRenderer.on('download-success', callback),
  onDownloadError: (callback) => ipcRenderer.on('download-error', callback),
  openExternalLink: (url) => ipcRenderer.send('open-external-link', url),
  openDownloadFolder: () => ipcRenderer.send('open-download-folder')
});
