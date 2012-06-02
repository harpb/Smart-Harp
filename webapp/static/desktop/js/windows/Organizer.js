/*!
 * Ext JS Library 4.0
 * Copyright(c) 2006-2011 Sencha Inc.
 * licensing@sencha.com
 * http://www.sencha.com/license
 */

Ext.define('MyDesktop.Organizer', {
    extend: 'Ext.ux.desktop.Module',

    requires: [
	    'Ext.org.ImageView',
	    'Ext.org.AlbumTree',
	    'Ext.org.OrgPanel',
	    'Ext.data.TreeStore',
	    'Ext.data.proxy.Ajax',
	    'Ext.tree.Column',
	    'Ext.tree.View',
	    'Ext.selection.TreeModel',
	    'Ext.tree.plugin.TreeViewDragDrop'
    ],

    id:'organizer',
    name: 'Image Organizer',

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
        	win = desktop.createWindow({
        		id: window_id,
	            title: this.name,
	            iconCls: 'icon-grid',
	            layout: 'fit',
	            maximized: true,
	            width: 480,
	            height: 240,
	        	items: [
	            {
                    xtype: 'panel',
		            layout: 'border',
		            items: [
			            {
			                xtype: 'albumtree',
			                region: 'west',
			                padding: 5,
			                width: 200
			            },
			            {
			                xtype: 'panel',
			                title: 'My Images',
			                layout: 'fit',
			                region: 'center',
			                padding: '5 5 5 0',
			                items: {
			                    xtype: 'imageview',
			                    /*  (add a '/' at the front of this line to turn this on)
			                    listeners: {
			                        containermouseout: function (view, e) {
			                            Ext.log('ct', e.type);
			                        },
			                        containermouseover: function (view, e) {
			                            Ext.log('ct', e.type);
			                        },
			                        itemmouseleave: function (view, record, item, index, e) {
			                            Ext.log('item', e.type, ' id=', record.id);
			                        },
			                        itemmouseenter: function (view, record, item, index, e) {
			                            Ext.log('item', e.type, ' id=', record.id);
			                        }
			                    },/**/
			                    trackOver: true
			                }
			            }
			        ]
			   }]
	        });
        }

        return win;
    }
});
