# Simple Dash App 


## Install App 

## Create Python Virtual Env 
```
python3 -m venv venv
```

## Activate environment 
```
source venv/bin/activate
```
## Install dependencies
```
$ (venv) pip install -r requirements.txt
```

## App Notes

```


Callbacks allows data to flow between components 
i.e. from the dropdown -> graph via user interaction
i.e. select a different country 


Syntax of Callback parameters (registers an output and input component for data flow)

Output(id, property)
Input(id, property)

Output('graph-content', 'figure'),
Input('dropdown-selection', 'value')

This @callback decorator applies to the update_graph

your function needs def update_
below it's called update_graph



```
