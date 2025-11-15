from odoo import http
class Vehicles(http.Controller):
    @http.route("/rentcars/allvehicles", type='http', auth='public', website=True)
    def list(self, **kwargs):
        Vehicle = http.request.env["rentcars.vehicle"]
        vehicles = Vehicle.search([])
        return http.request.render("rentcars.vehicle_list_template", {"vehicles": vehicles})