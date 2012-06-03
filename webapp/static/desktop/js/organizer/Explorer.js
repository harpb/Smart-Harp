/**
 * @class Ext.org.AlbumTree
 * @extends Ext.tree.Panel
 * @xtype albumtree
 *
 * This class implements the "My Albums" tree. In addition, this class provides the ability
 * to add new albums and accept dropped items from the {@link Ext.org.ImageView}.
 */
Ext.define('Ext.org.Explorer', {
    extend: 'Ext.panel.Panel',
    alias: 'widget.explorer',
    
	requires: [
	    'Ext.org.ImageView',
 	    'Ext.org.AlbumTree', ],
    
    layout: 'border',
    
    initComponent: function() {

		var filesPanel = Ext.create('Ext.panel.Panel', {
			title: 'My Images',
			id: 'files-panel', 
	        layout: 'fit',
	        region: 'center',
	        padding: '0 0 0 5',
	        items: {
	            xtype: 'imageview',
	            trackOver: true
	        }
		});
		
		eventHandler = function(){console.log("mouse over")}
		filesPanel.on({
		    cellClick: {fn: eventHandler, scope: this, single: true},
		    mouseover: {fn: eventHandler, scope: filesPanel}
		});
		
		var store =  Ext.create('Ext.data.TreeStore', {
           root: {
               expanded: true
           },
           proxy: {
               type: 'ajax',
               url: '/static/desktop/json/folders-data.json'
           }
       });
       
       // Go ahead and create the TreePanel now so that we can use it below
       var treePanel = Ext.create('Ext.tree.Panel', {
           id: 'tree-panel',
           title: 'Folders',
           region:'north',
           split: true,
           height: 240,
           minSize: 150,
           rootVisible: false,
           autoScroll: true,
           store: store
       });

       treePanel.getSelectionModel().on('select', function(selModel, record) {
           if (record.get('leaf')) {
        	   var feedType = record.data['id'] 
        	   var explorerContent = Ext.getCmp("explorer-content")
        	   explorerContent.getFeed(feedType);
           }
       });
       
       // This is the Details panel that contains the description for each example layout.
       var detailsPanel = {
           id: 'details-panel',
           title: 'Details',
           region: 'center',
           bodyStyle: 'padding-bottom:15px;background:#eee;',
           autoScroll: true,
           html: '<p class="details-info">When you select a layout from the tree, additional details will display here.</p>'
       };
		
       this.items = [{
               layout: 'border',
               id: 'layout-browser',
               region:'west',
               border: false,
               split:true,
               margins: '0 0 0 0',
               width: 275,
               minSize: 100,
               maxSize: 500,
               items: [treePanel, detailsPanel]
           }, 
               filesPanel
           ];
        
        this.callParent();
    },

});