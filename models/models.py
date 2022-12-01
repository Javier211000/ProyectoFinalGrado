from odoo import models, fields, api

class futbol_jugador(models.Model):
    _name = "futbol.jugador"

    name = fields.Char(string="Código del Jugador",required=True,help="Introduce el Código del Jugador:")
    NombreCompletoJugador = fields.Char(string="Nombre Completo del Jugador",required=True,help="Introduce el Nombre Completo del Jugador:")
    DorsalJugador = fields.Integer(string="Dorsal del Jugador",required=True,help="Introduce el Dorsal del Jugador:")
    EdadJugador = fields.Integer(string="Edad del Jugador",required=True,help="Introduce la Edad del Jugador:")
    PosicionJugador = fields.Char(string="Posición del Jugador",required=True,help="Introduce la Posición del Jugador:")
    PiernaBuenaJugador = fields.Char(string="Pierna Buena del Jugador",required=True,help="Introduce la Pierna Buena del Jugador:")
    JugadorRetirado = fields.Boolean(string="Jugador Retirado",required=True,help="Introduce si el Jugador está retirado o no:",default='False')
    URLJugador = fields.Char(string="Web Personal del Jugador",help="Introduce la Web Personal del Jugador:")
    ImagenJugador = fields.Binary('Imagen del Jugador')
    JugadoresTemporadas = fields.One2many("futbol.temporada","jugadores",string="JugadoresTemporadas")


class futbol_equipo(models.Model):
    _name = "futbol.equipo"

    name = fields.Char(string="Código del Equipo",required=True,help="Introduce el Código del Equipo:")
    NombreCompletoEquipo = fields.Char(string="Nombre Completo del Equipo",required=True,help="Introduce el Nombre Completo del Equipo:")
    CiudadDelEquipo = fields.Char(string="Ciudad del Equipo",required=True,help="Introduce la Ciudad del Equipo:")
    ProvinciaDelEquipo = fields.Char(string="Provincia del Equipo",required=True,help="Introduce la Provincia del Equipo:")
    SociosDelEquipo = fields.Integer(string="Socios del Equipo",required=True,help="Introduce los Socios del Equipo:")
    PresupuestoDelEquipo = fields.Integer(string="Presupuesto del Equipo",required=True,help="Introduce el Presupuesto del Equipo:")
    AnioCreacionEquipo = fields.Date(string="Año de Creación del Equipo",required=True,help="Introduce el Año de Creación del Equipo:")
    URLEquipo = fields.Char(string="Web del Equipo",help="Introduce la Web del Equipo:")
    ImagenEquipo = fields.Binary('Imagen del Equipo')
    EquiposTemporada = fields.One2many("futbol.temporada","equipos",string="EquiposTemporadas")

class futbol_temporada(models.Model):
    _name = "futbol.temporada"

    name = fields.Integer(string="Registro de Temporada del Jugador y del Equipo",required=True,help="Introduce el Registro de la Temporada del Jugador y del Equipo:")
    GolesJugadorEquipo = fields.Integer(string="Goles del Jugador en el Equipo",required=True,help="Introduce los Goles del Jugador en el Equipo:")
    AsistenciasJugadorEquipo = fields.Integer(string="Asistencias del Jugador en el Equipo",required=True,help="Introduce las Asistencias del Jugador en el Equipo:")
    AniosJugadorEquipo = fields.Char(string="Año de la Temporada",required=True,help="Introduce el Año de la Temporada:")
    jugadores = fields.Many2one("futbol.jugador",string="Jugadores",required=True,ondelete="cascade")
    equipos = fields.Many2one("futbol.equipo",string="Equipos",required=True,ondelete="cascade")
    GolesAsistenciasTotalesJugadorEquipo = fields.Integer(string="Goles y Asistencias Totales del Jugador en el Equipo",compute="_golesAsistenciasTotales",store=True)

    @api.depends('GolesJugadorEquipo','AsistenciasJugadorEquipo')
    def _golesAsistenciasTotales(self):
        for r in self:
            r.GolesAsistenciasTotalesJugadorEquipo = r.GolesJugadorEquipo + r.AsistenciasJugadorEquipo
