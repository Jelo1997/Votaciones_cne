from django.urls import path
from components import views

urlpatterns = [
    #############UI-ELEMENTS##################
    path('alerts',views.AlertsView.as_view(),name='uielements-alerts'),
    path('buttons',views.ButtonsView.as_view(),name='uielements-buttons'),
    path('cards',views.CardsView.as_view(),name='uielements-cards'),
    path('carousel',views.CarouselView.as_view(),name='uielements-carousel'),
    path('dropdowns',views.DropDownsView.as_view(),name='uielements-dropdowns'),
    path('grid',views.GridView.as_view(),name='uielements-grid'),
    path('images',views.ImagesView.as_view(),name='uielements-images'),
    path('lightbox',views.LightBoxView.as_view(),name='uielements-lightbox'),
    path('modals',views.ModalsView.as_view(),name='uielements-modals'),
    path('rangeslidebar',views.RangeSliderView.as_view(),name='uielements-rangeslidebar'),
    path('sessiontimeout',views.SessionTimeoutView.as_view(),name='uielements-sessiontimeout'),
    path('progressbars',views.ProgressBarsView.as_view(),name='uielements-progressbars'),
    path('sweetalert',views.SweetAlertView.as_view(),name='uielements-sweetalert'),
    path('tabs&accordians',views.TabsView.as_view(),name='uielements-tabs'),
    path('typography',views.TypoGraphyView.as_view(),name='uielements-typography'),
    path('video',views.VideoView.as_view(),name='uielements-video'),
    path('general',views.GeneralView.as_view(),name='uielements-general'),
    path('colors',views.ColorsView.as_view(),name='uielements-colors'),
    path('rating',views.RatingView.as_view(),name='uielements-rating'),
    path('utilities',views.UtilitiesView.as_view(),name='uielements-utilities'),
    path('offcanvas',views.OffcanvasView.as_view(),name='uielements-offcanvas'),

    ############FORMS###########################
    path('formelements',views.FormelementsView.as_view(),name='forms-formelements'),
    path('formvalidation',views.FormValidationView.as_view(),name='forms-formvalidation'),
    path('formadvanced',views.FormAdvancedView.as_view(),name='forms-formadvanced'),    
    path('formeditors',views.FormEditorsView.as_view(),name='forms-formeditors'),
    path('formfileupload',views.FormFileuploadView.as_view(),name='forms-formfileupload'),
    path('formxeditable',views.FormXeditableView.as_view(),name='forms-formxeditable'),
    path('formrepeater',views.FormRepeaterView.as_view(),name='forms-formrepeater'),
    path('formwizard',views.FormWizardView.as_view(),name='forms-formwizard'),
    path('formmask',views.FormMaskView.as_view(),name='forms-formmask'),

    ##############Charts##############
    path('morrischarts',views.MorrisChartsView.as_view(),name='charts-morrischarts'),
    path('chartistcharts',views.ChartistChartsView.as_view(),name='charts-chartistcharts'),
    path('chartjscharts',views.ChartjsChartsView.as_view(),name='charts-chartjscharts'),
    path('flotcharts',views.FlotChartsView.as_view(),name='charts-flotcharts'),
    path('jqueryknobcharts',views.JqueryKnobChartsView.as_view(),name='charts-jqueryknobcharts'),
    path('sparklinecharts',views.SparklineChartsView.as_view(),name='charts-sparklinecharts'),

    ###########Tables####################
    path('basictables',views.BasicTablesView.as_view(),name='tables-basictables'), 
    path('datatables',views.DataTablesView.as_view(),name='tables-datatables'),
    path('responsivetables',views.ResponsiveTablesView.as_view(),name='tables-responsivetables'),
    path('editabletables',views.EditableTablesView.as_view(),name='tables-editabletables'),

    ##############Icons##################
    path('materialdesign',views.MaterialDesignView.as_view(),name='icons-materialdesign'),
    path('fontawesome',views.FontAwesomeView.as_view(),name='icons-fontawesome'),
    path('ionicons',views.IonIconsView.as_view(),name='icons-ionicons'),
    path('themifyicons',views.ThemifyIconsView.as_view(),name='icons-themifyicons'),
    path('dripicons',views.DripIconsView.as_view(),name='icons-dripicons'),
    path('typicons',views.TypIconsView.as_view(),name='icons-typicons'),

    ############Maps#####################
    path('googlemaps',views.GoogleMapsView.as_view(),name='maps-googlemaps'),
    path('vectormaps',views.VectorMapsView.as_view(),name='maps-vectormaps'),
]    