from grafanalib.core import *


dashboard = Dashboard(
  title="EXAMPLE Stats",
  rows=[
    Row(panels=[
      Graph(
        title="Frontend latency ZZ",
        dataSource='InfluxDB',
        targets=[
          Target(
            expr='SELECT mean("value") FROM "measurement" WHERE $timeFilter GROUP BY time($__interval) fill(null)',
            legendFormat="0.5 quantile",
            refId='A',
          ),
        ],
        yAxes=single_y_axis(format=SECONDS_FORMAT),
      ),
    ]),
  ],
).auto_panel_ids()