Indico PDF Generator Plugin Documentation
________________________________________

Plugin Overview
The Indico PDF Generator Plugin (indico-pdf-generator) is a custom plugin developed to allow users to generate and print event notices in a chosen template format within an Indico instance. The plugin enables easy customization and integration into the Indico event details page, allowing event-specific data to be dynamically rendered into pre-designed templates.
Features:
•	Customizable PDF templates.
•	Dynamic rendering of event-specific data such as venue, date, time, and speaker details.
•	Easy integration with the Indico platform.
•	User-friendly interface with print functionality.
________________________________________

Installation Guide
Follow the steps below to install and configure the indico-pdf-generator plugin for a new Indico instance.

Step 1: Prerequisites
Ensure that your Indico instance meets the following requirements:
•	Indico Version: 2.0 or higher
•	Python: 3.7 or higher
•	Flask: Installed as part of the Indico environment

Step 2: Plugin Setup
1.	Clone the Plugin Repository:
Clone the indico-pdf-generator plugin repository into the plugins directory of your Indico instance:
cd dev/indico/src/plugins
git clone https://github.com/JJsupercoder/Indico-Notice-Generator-Plugin.git
2.	Navigate to the Plugin Directory:
cd indico-pdf-generator
3.	Install Plugin Dependencies:
Ensure that the required dependencies are installed by running:
pip install -r requirements.txt
4.	Configure setup.py:
The setup.py file should be correctly configured to ensure that the plugin is recognized and integrated into Indico:
5.	Configure MANIFEST.in:
Ensure that the MANIFEST.in file includes the required static and template files.
6.	Install the Plugin:
Install the plugin in the Indico environment by running:
pip install -e .

Step 3: Configure Indico to Load the Plugin
1.	Enable the Plugin:
Add the plugin name to the list of PLUGINS in your Indico configuration file (src/indico/indico.conf):
PLUGINS = {'indico_pdf_generator'}
2.	Add the indico.conf path to the INDICO_CONFIG variable
export INDICO_CONFIG="/home/jenson/dev/indico/src/indico/indico.conf"
This line would need to be added every time if ubuntu is restarted. To prevent this you can do the following:

1. Open your shell configuration file:
For Bash, run this command: 
nano ~/.bashrc
At the End of the file, add the following line for INDICO_CONFIG variable:
# Indico Conf Variable for pointing the location
export INDICO_CONFIG="/home/jenson/dev/indico/src/indico/indico.conf"
Save your changes by entering:
source ~/.bashrc
3.	Start your Postgresql and Redis-server:
Run these commands to start your PostgreSQL and Redis-server, or else Indico might not be able to run.
sudo service postgresql start
sudo service redis-server start
4.	Restart the Indico Server:
After making these changes, restart your Indico server to load the plugin:
indico run -h localhost -q --enable-evalex

Additionally, its recommended to compile the JS and style assets by running this command in another shell running parallelly:
(Ensure the current directory is src: cd dev/indico/src)
./bin/maintenance/build-assets.py indico --dev --watch

Step 4: Accessing the Plugin
1.	Plugin URL:
Once installed and enabled, the plugin is accessible at:
http://localhost:8000/pdf-generator-plugin/event/<event_id>

Where <event_id> is an integer like 2, 3, etc.
2.	Event Data Integration:
The plugin will dynamically fetch event-specific data (like venue, date, time, and speaker details) and render it into the templates. Ensure that event data is correctly entered while creating the event.
3.	Added a Button to Event Details Page:
On installing this plugin, a custom button, “Generate Notice” will be added into the Indico event details page that redirects users to the plugin's URL for generating PDFs.
      4.   Addition of an optional route for displaying all the Event Attributes and Event data
	You can view Event attributes and Event Data for any Indico Event by visiting:
http://localhost:8000/pdf-generator-plugin/event/<event_id>/params

This route can be removed from the blueprint.py if it’s found to be unnecessary. This route is retained only for viewing the attributes so that the you can add/modify event attributes in the blueprint.py, in case you want to display additional information about the events.

________________________________________

Screenshots of the Plugin:

![image](https://github.com/user-attachments/assets/1fbd3d44-379e-42a6-9a0c-920cfb68d773)

Indico Home Page with some existing Events 


![image](https://github.com/user-attachments/assets/8bc01feb-c574-4d3d-9206-d3ac109ff3f7)

Clicking on an Event to see details. Generate Notice Button appears at the bottom


![image](https://github.com/user-attachments/assets/64fd233f-541b-4d5e-a14c-3f901e64d0b1)

Clicking on the button redirects the user to the Plugin’s default generic.html page. 
 

![image](https://github.com/user-attachments/assets/03b925bd-867e-4dcd-b846-c880164564c1)

The user can choose a different template from the drop-down list


![image](https://github.com/user-attachments/assets/0bf33eda-cf7a-49e3-92ec-55a64b3017de)

The user can also increase or decrease the size of the notice to adjust for printing
 

![image](https://github.com/user-attachments/assets/7d0d7ac5-977b-4acf-a48c-4cb03c3d7c0d)

After adjusting the size, the user can easily print the PDF of the Notice

________________________________________

Key Files Overview
Here’s a quick overview of the key files and their purposes:
•	__init__.py: Main plugin class PDFGeneratorPlugin, template hooks, and event handlers.
•	blueprint.py: Contains Flask routes for fetching event data and rendering custom templates.
•	generic.html: The default template file used for generating event notices.
•	generic.css: CSS file for generic.html for styling the PDF output.
________________________________________

Final Notes
The indico-pdf-generator plugin is now fully functional and integrated with your Indico instance. For further customization or enhancement, you can modify the templates and CSS files within the plugin directory as per your requirements. You can also add more information about events in the notice, like speaker address, speaker contact no., etc. by passing a new event attribute variable to the html template. All event attributes can be viewed by visiting the additional route mentioned above. Ensure that any changes are thoroughly tested before deploying in a production environment.
For any issues or troubleshooting, kindly refer to the Indico documentation or reach out to the plugin's developer community.

You can also reach out to me, the Developer of this plugin.

