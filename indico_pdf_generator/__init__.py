from indico.core.plugins import IndicoPlugin
from flask import current_app, request
from indico.web.flask.util import url_for
from indico.web.flask.templating import TemplateSnippet
from indico.core import signals

class PDFGeneratorPlugin(IndicoPlugin):
    """Indico Notice Generator Plugin


    This plugin allows events to be displayed in custom templates for the purpose of printing out event notices. 
    It has features such as increasing or decreasing the size and also a button to print the pdf of the notice.
    """


    def init(self):
        super(PDFGeneratorPlugin, self).init()        
        self.connect(signals.plugin.template_hook, self._get_template_hooks)
        self.template_hook_map = {
                'event-header':self._render_generate_pdf_button,
                # 'event-page-header':self._render_generate_pdf_button, 
                # replace 'event-page-header' with another suitable template hook to add the generate notice button there
        }

        # To enable CSS styling on the templates by adding plugin template path
        with current_app.app_context():
            current_app.jinja_loader.searchpath.append(self.get_template_path())


    def _get_template_hooks(self, sender, **kwargs):
        renderer = self.template_hook_map.get(sender)
        if renderer:
            return renderer()

    def _render_generate_pdf_button(self, **kwargs):
        event_ID = request.view_args.get('event_id')
        # Generate the correct URL for the button
        event_pdf_url = url_for('plugin_indico_pdf_generator.event_pdf', event_id=event_ID)
        # Adding the button html
        return TemplateSnippet(
                f'''<div"><a class="i-button icon-edit" href="{event_pdf_url}" data-qtip-oldtitle="Use the plugin to select the template and generate the Notice PDF">Generate Notice</a></div>'''
                ,markup=True, priority=50)


    def get_blueprints(self):
        from .blueprint import plugin_blueprint
        return plugin_blueprint

    def get_template_path(self):
        return self.root_path + '/templates'


__all__ = ('PDFGeneratorPlugin',)


