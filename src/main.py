from paddlex import create_pipeline
import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="conf", config_name="default")
def main(cfg: DictConfig):
    pipeline = create_pipeline(pipeline=cfg.pipeline.type)
    output = pipeline.predict(cfg.input.image_path)
    for res in output:
        res.print()
        res.save_to_img(cfg.output.img_path)
        res.save_to_json(cfg.output.json_path)


if __name__ == "__main__":
    main()
