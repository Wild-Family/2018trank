const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow = null;

// app.on("window-all-closed", function() {
//     if (process.platform != "darwin") {
//         app.quit();
//     }
// });

app.on('ready', () => {
    mainWindow = new BrowserWindow({
        width: 700,
        height: 500,
    });
    mainWindow.loadURL('file://' + __dirname + '/index.html');
    mainWindow.webContents.openDevTools();
    mainWindow.on('closed', function() {
        mainWindow = null;
    });
});