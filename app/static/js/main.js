$(document).ready(function () {
  // ---------------- INIT ----------------
  $(".image-section").hide();
  $(".loader").hide();
  $("#result-card").hide();

  let dropArea = document.getElementById("drop-area");
  let fileInput = document.getElementById("imageUpload");

  // ---------------- IMAGE PREVIEW ----------------
  function readURL(input) {
    if (input.files && input.files[0]) {
      let reader = new FileReader();

      reader.onload = function (e) {
        $("#imagePreview").css(
          "background-image",
          "url(" + e.target.result + ")",
        );

        $("#imagePreview").hide();
        $("#imagePreview").fadeIn(650);
      };

      reader.readAsDataURL(input.files[0]);
    }
  }

  $("#imageUpload").change(function () {
    $(".image-section").show();
    $("#btn-predict").show();

    $("#result-card").hide();

    readURL(this);
  });

  // ---------------- PREDICT ----------------
  $("#btn-predict").click(function () {
    let form_data = new FormData($("#upload-file")[0]);

    $("#btn-predict").hide();
    $(".loader").show();

    $.ajax({
      type: "POST",
      url: "/predict",
      data: form_data,

      contentType: false,
      cache: false,
      processData: false,
      dataType: "json",

      success: function (data) {
        console.log("Prediction result:", data);

        $(".loader").hide();
        $("#btn-predict").show();

        $("#result-card").fadeIn(600);

        $("#crop").text("Crop: " + data.crop);
        $("#disease").text("Disease: " + data.disease);
        $("#confidence").text("Confidence: " + data.confidence + "%");
      },

      error: function (xhr, status, error) {
        console.error("Prediction error:", error);

        $(".loader").hide();
        $("#btn-predict").show();

        alert("Prediction failed. Check server.");
      },
    });
  });

  // ---------------- DRAG & DROP ----------------

  if (dropArea) {
    ["dragenter", "dragover"].forEach((eventName) => {
      dropArea.addEventListener(eventName, function (e) {
        e.preventDefault();
        dropArea.style.background = "#e6fff8";
      });
    });

    ["dragleave", "drop"].forEach((eventName) => {
      dropArea.addEventListener(eventName, function (e) {
        e.preventDefault();
        dropArea.style.background = "white";
      });
    });

    dropArea.addEventListener("drop", function (e) {
      let files = e.dataTransfer.files;

      if (files.length > 0) {
        fileInput.files = files;
        $("#imageUpload").trigger("change");
      }
    });
  }

  // ---------------- SHOW MORE DISEASES ----------------

  $("#show-more-btn").click(function () {
    $(".more-disease").slideToggle();

    if ($(this).text() === "Show More") {
      $(this).text("Show Less");
    } else {
      $(this).text("Show More");
    }
  });
});
