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


with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

