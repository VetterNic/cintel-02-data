import palmerpenguins
from shiny import render
from shiny import reactive, render, req
from shiny.express import input, ui
from shinywidgets import render_plotly
import shinyswatch

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

shinyswatch.theme.superhero()

#Title
ui.page_opts(title="Vetter M2 Penguins", fillable=True)


# Add a Shiny UI sidebar for user interaction
# Use the ui.sidebar() function to create a sidebar
# Set the open parameter to "open" to make the sidebar open by default
# Use a with block to add content to the sidebar
with ui.sidebar(open="open"):
    ui.h2("Sidebar")
    ui.hr()
    
# Use ui.input_selectize() to create a dropdown input to choose a column
#   pass in three arguments:
#   the name of the input (in quotes), e.g., "selected_attribute"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) 
#   e.g. ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    
    ui.input_selectize("selected_species", "Species Selected", 
                       ["Adelie", "Chinstrap", "Gentoo"])

# Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
#   pass in two arguments:
#   the name of the input (in quotes), e.g. "plotly_bin_count"
#   the label for the input (in quotes)
    
    ui.input_numeric("px_bin_count", "Bin Count", 10)

# Use ui.input_slider() to create a slider input for the number of Seaborn bins
#   pass in four arguments:
#   the name of the input (in quotes), e.g. "seaborn_bin_count"
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)
    ui.input_slider("sns_bin_count", "Sns Bin Count", 1, 100, 10)

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
#   pass in five arguments:
#   the name of the input (in quotes), e.g.  "selected_species_list"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#   a keyword argument selected= a list of selected options for the input (in square brackets)
#   a keyword argument inline= a Boolean value (True or False) as you like
    ui.input_checkbox_group("species_selected","Select Species", 
                            ["Adelie", "Gentoo", "Chinstrap"],
                            selected=["Adelie", "Gentoo", "Chinstrap"])

with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

