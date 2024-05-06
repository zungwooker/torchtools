from collections import OrderedDict
import torch

# model_args = OrderedDict()
# model_args['model_type'] = 'MLP'
# model_args['dataset'] = 'CMNISTZW'
# model_args['lr'] = 0.001
# model_args['epochs'] = 100
# model_args['trainigtime'] = '1h23m'
# model_args['projcode'] = 'TESTEST'

def savemodel(model, model_args: OrderedDict, save_dir='/mnt/sdc/zungwooker/workspace/debiasing/data/output/models/'):
    model_name = f"{model_args['model_type']}_{model_args['dataset']}"
    for key in model_args.keys():
        if key not in ['model_type', 'dataset']:
            model_name += f"_{key}{model_args[key]}"
            
    model.eval()
    torch.save(model.state_dict(), f"{save_dir}{model_name}.pth")