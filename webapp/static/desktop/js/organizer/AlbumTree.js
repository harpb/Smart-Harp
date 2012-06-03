/**
 * @class Ext.org.AlbumTree
 * @extends Ext.tree.Panel
 * @xtype albumtree
 *
 * This class implements the "My Albums" tree. In addition, this class provides the ability
 * to add new albums and accept dropped items from the {@link Ext.org.ImageView}.
 */
Ext.define('Ext.org.AlbumTree', {
    extend: 'Ext.tree.Panel',
    alias : 'widget.albumtree',
    
    title: 'My Albums',
    animate: true,
    rootVisible: false,
    
    viewConfig: {
        plugins: [{
            ddGroup: 'organizerDD',
            ptype  : 'treeviewdragdrop'
        }]
    },
    
    displayField: 'name',
    
    initComponent: function() {
	
        this.items = [
	        {
	            // Explicitly define the xtype of this Component configuration.
	            // This tells the Container (the tab panel in this case)
	            // to instantiate a Ext.panel.Panel when it deems necessary
	            xtype: 'panel',
	            title: 'Tab One',
	            html: 'The first tab',
	            listeners: {
	                render: function() {
	                    Ext.MessageBox.alert('Rendered One', 'Tab One was rendered.');
	                }
	            }
	        },
	        {
	            // this component configuration does not have an xtype since 'panel' is the default
	            // xtype for all Component configurations in a Container
	            title: 'Tab Two',
	            html: 'The second tab',
	            listeners: {
	                render: function() {
	                    Ext.MessageBox.alert('Rendered One', 'Tab Two was rendered.');
	                }
	            }
	        }
	    ];
        
        this.callParent();
    },
    
	/**
     * Create the context menu
     * @private
     */
    createMenu: function(){
        this.menu = Ext.create('widget.menu', {
            items: [{
                scope: this,
                handler: this.onLoadClick,
                text: 'Load feed',
                iconCls: 'feed-load'
            }, this.removeAction, '-', this.addAction],
            listeners: {
                hide: function(c){
                    c.activeFeed = null;
                }
            }
        });
    },
    
    /**
     * React to the load feed menu click.
     * @private
     */
    onLoadClick: function(){
        this.loadFolder(this.menu.activeFeed);
    },

    /**
     * Loads a feed.
     * @private
     * @param {Ext.data.Model} rec The feed
     */
    loadFolder: function(rec){
        if (rec) {
            this.fireEvent('folder_select', this, rec.get('title'), rec.get('url'));
        }
    },
});