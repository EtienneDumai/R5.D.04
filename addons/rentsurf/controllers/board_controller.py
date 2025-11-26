from odoo import http
class Board(http.Controller):
    @http.route("/rentsurf/allboards", type='http', auth='public', website=True)
    def list(self, **kwargs):
        Board = http.request.env["rentsurf.board"]
        boards = Board.search([])
        return http.request.render("rentsurf.board_list_template", {"boards": boards})