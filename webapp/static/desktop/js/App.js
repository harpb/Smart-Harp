Ext.Loader.setPath({
    'Ext.ux.desktop': '/static/desktop/js/desktop',
    'MyDesktop': '/static/desktop/js/windows',
    'Ext.org': '/static/desktop/js/organizer',
    'Ext.ux.DataView': '/static/desktop/js/DataView',
});

Ext.Loader.setConfig({enabled:true});

Ext.require('MyDesktop.App');

var myDesktopApp;
Ext.onReady(function () {
    myDesktopApp = new MyDesktop.App();
});