import os
import unittest
from unittest import mock
from bottle import FormsDict
import plotting_func

class LinearFunctionTestCase(unittest.TestCase):
    @mock.patch('plotting_func.template')
    @mock.patch('plotting_func.bottle.request')
    def test_linear_function(self, mock_request, mock_template):
        mock_template.return_value = "Mocked template"

        form_data = FormsDict()
        form_data['function'] = 'linear'
        form_data['k_coefficient'] = '2'
        form_data['b_coefficient'] = '3'
        form_data['start_length'] = '0'
        form_data['end_length'] = '10'

        mock_request.forms.get.side_effect = form_data.get
        mock_request.environ = {'wsgi.input': mock.Mock()}

        plotting_func.handle_plot_request()

        expected_image_data = os.path.join('static', 'images', 'graph1.png')
        mock_template.assert_called_once_with('plotting.tpl', message="", image_data=expected_image_data, title='Построение графиков', year=mock.ANY)


class QuadraticFunctionTestCase(unittest.TestCase):    
    @mock.patch('plotting_func.template')
    @mock.patch('plotting_func.bottle.request')    
    def test_quadratic_function(self, mock_request, mock_template):
        mock_template.return_value = "Моковый шаблон"
        form_data = FormsDict()        
        form_data['function'] = 'quadratic'
        form_data['a_coefficient'] = '1'        
        form_data['b_coefficient'] = '2'
        form_data['c_coefficient'] = '3'        
        form_data['start_length'] = '0'
        form_data['end_length'] = '10'
        mock_request.forms.get.side_effect = form_data.get        
        mock_request.environ = {'wsgi.input': mock.Mock()}
        plotting_func.handle_plot_request()
        expected_image_data = os.path.join('static', 'images', 'graph1.png')
        mock_template.assert_called_once_with('plotting.tpl', message="", image_data=expected_image_data, title='Построение графиков', year=mock.ANY)


class PowerFunctionTestCase(unittest.TestCase):
    @mock.patch('plotting_func.template')
    @mock.patch('plotting_func.bottle.request')
    def test_power_function(self, mock_request, mock_template):
        mock_template.return_value = "Mocked template"

        form_data = FormsDict()
        form_data['function'] = 'power'
        form_data['a_coefficient'] = '2'
        form_data['start_length'] = '0'
        form_data['end_length'] = '10'

        mock_request.forms.get.side_effect = form_data.get
        mock_request.environ = {'wsgi.input': mock.Mock()}

        plotting_func.handle_plot_request()

        expected_image_data = os.path.join('static', 'images', 'graph1.png')
        mock_template.assert_called_once_with('plotting.tpl', message="", image_data=expected_image_data, title='Построение графиков', year=mock.ANY)
