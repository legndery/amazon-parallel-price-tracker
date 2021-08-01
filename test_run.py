TEST_VAL='report_generator_abstract'

if TEST_VAL == 'report_generator_abstract':
  from modules.repository.sql_repository import SqlRepository, Base
  from modules.report_generator_abstract import ReportGenerator

  product_arr = [{"asin":"B07YFF3JCN", "title":"Western Digital WD SN550 500GB NVMe Internal SSD - 2400MB/s R, 1750MB/s W, (WDS500G2B0C, Blue)"}]
  ReportGenerator(SqlRepository(Base), product_arr).plot_graph(product_arr[0])
