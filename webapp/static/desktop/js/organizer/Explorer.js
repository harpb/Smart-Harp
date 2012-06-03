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
	           'Ext.org.ExplorerContent',
	           'Ext.org.AlbumTree', 
	           'Ext.org.ImagePanel',
 	],
    
    layout: 'border',
    
    initComponent: function() {

		var filesPanel = Ext.create('Ext.panel.Panel', {
			id: 'files-panel', 
	        layout: 'fit',
	        region: 'center',
	        padding: '0 0 0 5',
		    width: 160,
	        items: {
	            xtype: 'explorercontent',
	            name: "List of Files",
//	            trackOver: true,
	            listeners: {
	            	scope: this,
	            	selectionchange: this.onFileSelect,
//	            	itemdblclick: this.fireFileOpen
	            }
	        },
		});
		var store =  Ext.create('Ext.data.TreeStore', {
           root: {
               expanded: true,
               activeItem: 1
           },
           activeItem: 1,
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
           activeGroup: 1,
           activeItem: 'photo_feed',
           split: true,
           height: '50%',
           minSize: 150,
           rootVisible: false,
           autoScroll: true,
           expanded: true,
           store: store,
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
           html: '<p class="details-info">Eventually, additional details will display here.</p>'
       };

       this.previewPanel = Ext.create('Ext.org.ImagePanel', {
           id: 'preview-panel',
           region:'east',
           split: true,
           width: '70%',
           title: 'Preview',
		   collapsible: true,
           rootVisible: false,
           autoScroll: true,
           expanded: true,
       });
       this.previewPanel.hide();
       
       this.items = [{
               layout: 'border',
               id: 'layout-browser',
               region:'west',
               border: false,
               split:true,
               margins: '0 0 0 0',
               width: 140,
               items: [treePanel, detailsPanel]
           }, 
               filesPanel,
               this.previewPanel
           ];
        
        this.callParent();
    },
    
    onFileSelect: function(dataview, selections) {
        var selected = selections[0];
        
        if (selected) {
//            this.down('preview-panel').loadRecord(selected);
        	if(selected.data.type == 'video')
			{
				window.open(selected.data.url);
				this.previewPanel.hide();
			}
        	else{
        		Ext.getCmp('preview-panel').show();
        		Ext.getCmp('preview-panel').loadRecord(selected);
        	}
        }
    },

});