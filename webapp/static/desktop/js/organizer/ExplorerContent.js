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
Ext.define('Ext.org.ExplorerContent', {
    extend: 'Ext.view.View',
    alias : 'widget.explorercontent',
    requires: [
               'Ext.data.Store',
               'Ext.org.ImageViewer',
              ],
//    mixins: {
//        dragSelector: 'Ext.ux.DataView.DragSelector',
//        draggable   : 'Ext.ux.DataView.Draggable'
//    },

    id: 'explorer-content',
    
    tpl: [
        '<tpl for=".">',
            '<a class="thumb-wrap" target="_blank">',
                '<div class="thumb">',
                    (!Ext.isIE6? '<img src="{thumbnail_url}" />' : 
                    '<div style="width:76px;height:76px;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'../view/chooser/icons/{thumb}\')"></div>'),
                '</div>',
                '<span><img src="/static/desktop/icons/services/{service}.gif"> {name}</span>',
            '</a>',
        '</tpl>'
    ],
    
    itemSelector: 'a.thumb-wrap',
//    multiSelect: true,
    singleSelect: true,
    cls: 'x-explorer-content',
    autoScroll: true,
    
    initComponent: function() {
		
        this.store = Ext.create('Ext.data.Store', {
//            autoLoad: true,
//        	pageSize: 5,
            fields: ['description', 'name', 'service', 'thumbnail_url', 'type', 'url'],
            proxy: {
                type: 'ajax',
                url : '/rest/v1/',
                reader: {
                    type: 'json',
                    root: 'objects'
                }
            }
        });
        
//        this.store.loadPage(2);

//		this.listeners = {
//				itemclick: function(source, record) {
//					console.log(source);
//					console.log(record);
//					if(record.data.type == 'video')
//					{
//						window.open(record.data.url);
//					}
//					else{
//						console.log("Open Image Viewer: " + record);
//					}
//				}
//			};
			
	   this.callParent();
	},

		getFeed: function(feedType){
    		var feeds = {
				'photo': '/photo/',
				'photo_feed': '/photo_feed/',
				'video': '/video/',
				'video_feed': '/video_feed/',
    		
    		}
    		var endpoint = feeds[feedType];
			this.store.proxy.url = '/rest/v1/' + feedType +'/'
			params = {start:0, limit:100};
//			console.log(this.store)
			this.store.load({params: params});	
		},
});