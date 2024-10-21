from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

############UI-ELEMENTS####################
class AlertsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "Alerts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-alerts.html',greeting)

class ButtonsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Buttons"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-buttons.html',greeting)

class CardsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Cards"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-cards.html',greeting)          

class CarouselView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Carousel"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-carousel.html',greeting)          

class DropDownsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dropdowns"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-dropdowns.html',greeting)       

class GridView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Grid"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-grid.html',greeting)              

class ImagesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Images"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-images.html',greeting)           

class LightBoxView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Lightbox"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-lightbox.html',greeting)          

class ModalsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Modals"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-modals.html',greeting)          

class RangeSliderView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Range Slider"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-rangeslidebar.html',greeting)       

class SessionTimeoutView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Session Timeout"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-sessiontimeout.html',greeting)               

class ProgressBarsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Progress Bars"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-progressbars.html',greeting)   

class SweetAlertView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = " Sweet Alert 2"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-sweetalert.html',greeting)                  

class TabsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Tabs & Accordions"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-tabs.html',greeting)   

class TypoGraphyView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Typography"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-typography.html',greeting)  

class VideoView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Video"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-video.html',greeting)     

class GeneralView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "General"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-general.html',greeting) 

class ColorsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Colors"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-colors.html',greeting)  

class RatingView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Rating"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-rating.html',greeting) 

class UtilitiesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Utilities"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-utilities.html',greeting)
    
    
class OffcanvasView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Offcanvas"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-offcanvas.html',greeting)

############FORMS###########################                 

class FormelementsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Elements"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formelements.html',greeting)   

class FormValidationView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Validation"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formvalidation.html',greeting)      

class FormAdvancedView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Advanced"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formadvanced.html',greeting) 

class FormEditorsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Editors"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formeditors.html',greeting)  

class FormFileuploadView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form File Upload"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formfileupload.html',greeting) 

class FormXeditableView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Xeditable"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formxeditable.html',greeting)           

class FormRepeaterView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Repeater"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formrepeater.html',greeting)         

class FormWizardView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Wizard"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formrwizard.html',greeting)                  
        
class FormMaskView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Mask"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formrmask.html',greeting) 

############Charts######################                 

class MorrisChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Morris Charts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-morrischarts.html',greeting)     

class ChartistChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Chartist Charts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-chartistcharts.html',greeting)     

class ChartjsChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Chartjs Charts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-chartjscharts.html',greeting) 

class FlotChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Flot Charts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-flotcharts.html',greeting)    

class JqueryKnobChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Jquery Knob Charts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-jqueryknobcharts.html',greeting)                                       

class SparklineChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Sparkline Charts"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-sparklinecharts.html',greeting)   

######Tables##########
class BasicTablesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Basic Tables"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-basictables.html',greeting)         

class DataTablesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Data Tables"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-datatables.html',greeting) 

class ResponsiveTablesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Responsive Table"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-responsivetables.html',greeting)  

class EditableTablesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Editable Table"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-editabletables.html',greeting)   

###########Icons################  
class MaterialDesignView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Material Design"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-materialdesign.html',greeting)  

class FontAwesomeView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Font Awesome"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-fontawesome.html',greeting)     

class IonIconsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Ion Icons"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-ionicons.html',greeting)  

class ThemifyIconsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Themify Icons"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-themifyicons.html',greeting)   

class DripIconsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dripicons"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-dripicons.html',greeting)          

class TypIconsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Typicons Icons"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-typicons.html',greeting)    

###########Maps###############
class GoogleMapsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Google Maps"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Maps"
        return render (request,'components/maps/maps-googlemaps.html',greeting)                                            

class VectorMapsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Vector Maps"
        greeting['heading'] = "Proyecto_votacion"
        greeting['subheading'] = "Maps"
        return render (request,'components/maps/maps-vectormaps.html',greeting)

               