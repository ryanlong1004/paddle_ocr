import unittest
from unittest.mock import patch, MagicMock
from main import main


class TestMain(unittest.TestCase):

    @patch("main.create_pipeline")
    @patch("main.hydra.main")
    def test_main(self, mock_hydra_main, mock_create_pipeline):
        # Mock the configuration
        cfg = MagicMock()
        cfg.pipeline.type = "OCR"
        cfg.input.image_path = "./sign_text.png"
        cfg.output.img_path = "./output/"
        cfg.output.json_path = "./output/"

        # Mock the pipeline and its output
        mock_pipeline = MagicMock()
        mock_create_pipeline.return_value = mock_pipeline
        mock_output = [MagicMock()]
        mock_pipeline.predict.return_value = mock_output

        # Run the main function
        main(cfg)

        # Assertions
        mock_create_pipeline.assert_called_once_with(pipeline="OCR")
        mock_pipeline.predict.assert_called_once_with("./sign_text.png")
        for res in mock_output:
            res.print.assert_called_once()
            res.save_to_img.assert_called_once_with("./output/")
            res.save_to_json.assert_called_once_with("./output/")


if __name__ == "__main__":
    unittest.main()
