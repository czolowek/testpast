from sqlalchemy import Table, Column, ForeignKey
from data.base import Base


pizza_ingred_assoc = Table("pizza_ingred_assoc",
Base.metadata,
Column("pizza_id", ForeignKey("pizzas.id"), primary_key=True),
Column("ingredient_id", ForeignKey("ingredients.id"), primary_key=True)
)