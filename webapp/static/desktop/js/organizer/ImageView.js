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
Ext.define('Ext.org.ImageView', {
    extend: 'Ext.view.View',
    alias : 'widget.imageview',
    requires: ['Ext.data.Store'],
//    mixins: {
//        dragSelector: 'Ext.ux.DataView.DragSelector',
//        draggable   : 'Ext.ux.DataView.Draggable'
//    },

    id: 'explorer-content',
    
    tpl: [
        '<tpl for=".">',
            '<a class="thumb-wrap" href="{url}" target="_blank">',
                '<div class="thumb">',
                    (!Ext.isIE6? '<img src="{thumbnail_url}" />' : 
                    '<div style="width:76px;height:76px;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'../view/chooser/icons/{thumb}\')"></div>'),
                '</div>',
                '<span>{name}</span>',
            '</a>',
        '</tpl>'
    ],
    
    itemSelector: 'a.thumb-wrap',
//    multiSelect: true,
    singleSelect: true,
    cls: 'x-image-view',
    autoScroll: true,
    
    initComponent: function() {
        this.store = Ext.create('Ext.data.Store', {
//            autoLoad: true,
            fields: ['name', 'thumbnail_url', 'url'],
            proxy: {
                type: 'ajax',
                url : '/rest/v1/',
                reader: {
                    type: 'json',
                    root: 'objects'
                }
            }
        });
        
		eventHandler = function(){console.log("THE mouse over")}
		this.on({
		    cellClick: {fn: eventHandler, scope: this, single: true},
		    mouseover: {fn: eventHandler, scope: this}
		});
		
		//listen for node click?
		this.on("click", function(vw, index, node, e){
		alert('Node "' + node.id + '" at index: ' + index + " was clicked.");
		});
        
//        this.mixins.dragSelector.init(this);
//        this.mixins.draggable.init(this, {
//            ddConfig: {
//                ddGroup: 'organizerDD'
//            },
//            ghostTpl: [
//                '<tpl for=".">',
//                    '<img src="../view/chooser/icons/{thumb}" />',
//                    '<tpl if="xindex % 4 == 0"><br /></tpl>',
//                '</tpl>',
//                '<div class="count">',
//                    '{[values.length]} images selected',
//                '<div>'
//            ]
//        });
		//trigger the data store load
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
			params = {start:0, limit:25};
//			console.log(this.store)
			this.store.load({params: params});	
		},
});