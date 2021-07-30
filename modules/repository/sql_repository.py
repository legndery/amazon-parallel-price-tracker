from modules.repository.repository import Repository


from modules.repository.repository import Repository

class SqlRepository(Repository):
  def __init__(self):
    super().__init__()
  def get_last_product(self, product_id):
      return super().get_last_product(product_id)
  def append_product(self, product):
      return super().append_product(product)
  def up(self):
      return super().up()