/**
 * @class Ext.org.ImageView
 * @extends Ext.view.View
 * @xtype imageview
 *
 * This class implements the "My Images" view (the images in the organizer). This class
 * incorporates {@link Ext.ux.DataView.Draggable Draggable} to enable dragging items as
 * well as {@link Ext.ux.DataView.DragSelector DragSelector} to allow multiple selection
 * by simply clicking and dragging the mouse.
 */
Ext.define('MyDesktop.ImageViewerWindow', {
	extend: 'Ext.ux.desktop.Module',
    alias : 'widget.imageviewer',
    requires: [
               'Ext.data.Store',
              ],
              
    id: 'image-viewer',
    name: 'Image Viewer',
    cls: 'x-image-viewer',
    
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
	    	explorer = Ext.create('Ext.panel.Panel', {});
	    	win = desktop.createWindow({
	    		id: window_id,
	            title: this.name,
	            iconCls: 'icon-grid',
	            layout: 'fit',
	            maximized: true,
	            width: 480,
	            height: 240,
	        });
	    }
	
	    return win;
	}
});
