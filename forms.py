from wtforms import StringField, Form, SubmitField
from wtforms.validators import DataRequired


class SearchForm(Form):
  query = StringField('query', [DataRequired()], render_kw={"placeholder": "Enter text to search entities..."})
  submit = SubmitField('Search',
                       render_kw={'class': 'btn btn-success btn-block'})

  def validate_on_submit(self):
      return self.query.data