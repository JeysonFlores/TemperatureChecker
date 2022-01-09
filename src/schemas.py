from __main__ import ma

class TemperaturesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'temp', 'date', 'time')
