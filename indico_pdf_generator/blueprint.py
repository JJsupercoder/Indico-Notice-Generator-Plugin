from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint #line added
from flask import render_template, request, Response #, Blueprint
import json
import os
from flask import current_app
from indico.modules.events import Event


plugin_blueprint = IndicoPluginBlueprint('indico_pdf_generator', __name__, url_prefix='/pdf-generator-plugin', static_folder='static')


@plugin_blueprint.route('/event/<int:event_id>', methods=['GET', 'POST'])
def event_pdf(event_id):
    # Fetch the event data based on the event_id passed from the button click
    event = Event.get_or_404(event_id)
    try:
        # user has selected another template
        selected_option = request.form["view"]
    except:
        # user loads the default page - generic.html before selecting template
        selected_option = "generic.html"

    selected_template_path = "indico_pdf_generator/"+selected_option
    try:
        speaker = event.sorted_person_links[0].name
        speaker_design = event.sorted_person_links[0].affiliation
    except IndexError:
        speaker = ""
        speaker_design = ""
    # Pass the event data to your custom HTML template
    return render_template(selected_template_path,
        speaker=speaker,
        speaker_designation=speaker_design,
        title=event.title,
        date=event.start_dt.strftime('%Y-%m-%d'),
        time=event.start_dt.strftime('%H:%M'),
        venue=event.own_venue_name,
        abstract=event.description,
        event=event,
    )


# this route is defined to view all the event attributes. you can remove this route if not required.
@plugin_blueprint.route('/event/<int:event_id>/params', methods=['GET'])
def event_debug(event_id):
    event = Event.get_or_404(event_id)
    event_attributes = dir(event)  # Get all attributes and methods of the event object
    event_data = vars(event)       # Get the __dict__ of the event object, showing its current data

    # Render the attributes and data as a simple string (or JSON) for inspection
    return f"Event Attributes: {event_attributes}<br><br>Event Data: {event_data}"



def read_json(json_file="data.json"):
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script's directory
    file_path = os.path.join(current_dir, json_file)  # Construct the absolute pat
    
    # Open the JSON file
    with open(file_path) as file:
        data = json.load(file)  # Load the JSON data
    return data


