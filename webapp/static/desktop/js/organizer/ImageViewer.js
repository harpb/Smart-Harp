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
Ext.define('Ext.org.ImageViewer', {
	extend: 'Ext.panel.Panel',
    alias : 'widget.imageviewer',
              
    id: 'image-viewer',
    name: 'Image Viewer',
    cls: 'x-image-viewer',
    
    layout: 'border',
    
	initComponent: function() {
		this.imagesPanel =  {
			region: 'east',
		    collapsible: true,
		    title: 'Images',
		    split: true,
		    width: 160,
		    html: 'List of Images'
		};
		
		this.viewer =  {
			region: 'center',
			html: 'center center',
			minHeight: 80,
	  	};
		this.items = [this.imagesPanel, this.viewer];
	 
		this.callParent();
	},
});
