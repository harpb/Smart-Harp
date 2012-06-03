/**
 * @class Ext.chooser.InfoPanel
 * @extends Ext.panel.Panel
 * @author Ed Spencer
 * 
 * This panel subclass just displays information about an image. We have a simple template set via the tpl property,
 * and a single function (loadRecord) which updates the contents with information about another image.
 */
Ext.define('Ext.org.ImagePanel', {
    extend: 'Ext.panel.Panel',
    alias : 'widget.imagepanel',
    id: 'img-detail-panel',

    width: 150,
    minWidth: 150,

    tpl: [
        '<div class="details" style="text-align: center; ">',
            '<tpl for=".">',
            	'<img src="{url}" />',                
            '</tpl>',
        '</div>'
    ],
    
    afterRender: function(){
        this.callParent();
        this.el.on('click', function(){
            alert('Nothing to do');
        }, this, {delegate: 'a'});
    },

    /**
     * Loads a given image record into the panel. Animates the newly-updated panel in from the left over 250ms.
     */
    loadRecord: function(image) {
    	this.title = image.data.title;
        this.body.hide();
        this.tpl.overwrite(this.body, image.data);
        this.body.slideIn('l', {
            duration: 250
        });
    }
});