def option_check(args):
    prompt = "Continue Training? (y/n): "

    print("\n==============================")
    print("Process details:")
    print(("------------------------------"))
    print(f"seed: {args.seed}")
    print(f"cuda: {args.cuda}")
    print(f"device: {args.device} \n")

    print(("------------------------------"))
    print("Training details:")
    print(("------------------------------"))
    print(f"epochs: {args.epochs}")
    print(f"LR: {args.lr}")
    print(f"batch size: {args.batch_size}")
    print(f"dataset: {args.dataset}")
    print(f"conflict ratio: {args.conflict_ratio}")
    print(f"save: {args.save} \n")

    print(("------------------------------"))
    print("Logging details:")
    print(("------------------------------"))
    print(f"remote: {args.remote}")
    print(f"run name: {args.run_name}")
    print(f"proj name: {args.project_name}")
    print("==============================\n")

    while True:
        response = input(prompt)
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            continue