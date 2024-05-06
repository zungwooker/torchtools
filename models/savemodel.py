from collections import OrderedDict
import torch

# args = OrderedDict()
# args['model_type'] = 'MLP'
# args['dataset'] = 'CMNISTZW'
# args['lr'] = 0.001
# args['epochs'] = 100
# args['trainigtime'] = '1h23m'
# args['projcode'] = 'TESTEST'

def savemodel(model, args: OrderedDict, save_dir='/mnt/sdc/zungwooker/workspace/debiasing/data/output/models/'):
    model_name = f"{args['model_type']}_{args['dataset']}"
    for key in args.keys():
        if key not in ['model_type', 'dataset']:
            model_name += f"_{key}{args[key]}"
            
    model.eval()
    torch.save(model.state_dict(), f"{save_dir}{model_name}.pth")