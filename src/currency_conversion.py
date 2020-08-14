import json
import click
from currency_converter import CurrencyConverter

@click.command()
@click.option('--amount', default=1, help='This tool helps convert currencies')
@click.option('--convertfrom', prompt='Enter the current Currency code', help='defaults to USD')
@click.option('--convertto', prompt='Enter the Target Currency Code', help='defaults to EUR')

def action(amount,convertfrom, convertto):
    cash = CurrencyConverter()
    if(convertfrom == ''):
        convertfrom='USD'
    if(convertto == ''):
        convertto='EUR'
    result = cash.convert(100, convertfrom, convertto)
    click.echo(click.style(f'{result}', bg='green', fg='white'))
    
if __name__=='__main__':
    action()