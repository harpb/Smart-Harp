/*!
 * Ext JS Library 4.0
 * Copyright(c) 2006-2011 Sencha Inc.
 * licensing@sencha.com
 * http://www.sencha.com/license
 */

Ext.define('MyDesktop.PhotosWindow', {
    extend: 'Ext.ux.desktop.Module',

    requires: [
	    'Ext.org.Explorer',
	    'Ext.data.TreeStore',
	    'Ext.data.proxy.Ajax',
	    'Ext.tree.Column',
	    'Ext.tree.View',
	    'Ext.selection.TreeModel',
	    'Ext.tree.plugin.TreeViewDragDrop'
    ],

    id:'photos_window',
    name: 'Photos',

    init : function(){
        this.launcher = {
            text: this.name,
            iconCls:'icon-grid'
        };
    },

    createWindow : function(){
        var desktop = this.app.getDesktop();
        var window_id = this.id +'-win'
        var win = desktop.getWindow(window_id);
        
        if (!win) {
//            win = Ext.create('Ext.org.OrgPanel', {
        	explorer = Ext.create('Ext.org.Explorer', {});
        	win = desktop.createWindow({
        		id: window_id,
	            title: this.name,
	            iconCls: 'icon-grid',
	            layout: 'fit',
	            maximized: true,
	            width: 480,
	            height: 240,
	        	items:   [
	            {
	                xtype: 'explorer',
	            }
	        ]
	        });
        }

        return win;
    }
});
