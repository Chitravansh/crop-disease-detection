$(document).ready(function () {
  // ---------------- INIT ----------------
  $(".image-section").hide();
  $(".loader").hide();
  $("#result-card").hide();

  let dropArea = document.getElementById("drop-area");
  let fileInput = document.getElementById("imageUpload");

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

        // 🔥 NEW: Trigger chatbot smart prompt
        triggerChatbotPrompt();
      },

      error: function (xhr, status, error) {
        console.error("Prediction error:", error);

        $(".loader").hide();
        $("#btn-predict").show();

        alert("Prediction failed. Check server.");
      },
    });
  });

  // ---------------- CHATBOT SMART PROMPT ----------------

  function triggerChatbotPrompt() {
    const chatBox = document.getElementById("chat-box");

    // If chatbot not present (user not on chatbot page), skip safely
    if (!chatBox) return;

    // Open chatbot widget automatically
    const chatWindow = document.getElementById("chat-window");
    const chatIcon = document.getElementById("chat-icon");
    const chatToggle = document.getElementById("chat-toggle");

    if (chatWindow && chatWindow.style.display !== "flex") {
      chatWindow.style.display = "flex";

      if (chatIcon) {
        chatIcon.classList.remove("fa-robot");
        chatIcon.classList.add("fa-xmark");
      }

      if (chatToggle) {
        chatToggle.classList.add("chat-open");
      }
    }

    // Add smart bot message with inline button
    addMessage(
      `
🌿 I detected a disease in your crop.

Do you want treatment suggestions?

<button onclick="getAdvisory()" class="btn btn-sm btn-success mt-2">
Yes, Show Treatment
</button>
`,
      "bot",
    );
  }

  // ---------------- GLOBAL FUNCTION (IMPORTANT) ----------------
  window.getAdvisory = async function () {
    const chatBox = document.getElementById("chat-box");

    if (!chatBox) return;

    showTyping();

    try {
      const response = await fetch("/api/advisory", {
        method: "POST",
      });

      const data = await response.json();

      removeTyping();

      if (data.reply) {
        addMessage(data.reply, "bot");
      } else {
        addMessage("⚠️ Unable to fetch advisory.", "bot");
      }
    } catch (err) {
      console.error("Advisory error:", err);
      removeTyping();
      addMessage("⚠️ Error fetching advisory. Try again.", "bot");
    }
  };

  // ---------------- GEOLOCATION ----------------

  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      async function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        try {
          // Reverse geocoding (free API)
          const res = await fetch(
            `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`,
          );

          const data = await res.json();

          const city =
            data.address.city ||
            data.address.town ||
            data.address.village ||
            "Your Area";

          await fetch("/api/location", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              city,
              latitude,
              longitude,
            }),
          });

          console.log("Location stored:", city);
        } catch (err) {
          console.error("Location fetch error:", err);
        }
      },
      function (error) {
        console.warn("Geolocation denied or failed.");
      },
    );
  }

  // ---------------- FLASH MESSAGE ----------------
  setTimeout(function () {
    $(".alert").fadeOut("slow");
  }, 4000);

  // ---------------- SHOW MORE DISEASES ----------------

  $("#show-more-btn").click(function () {
    $(".more-disease").slideToggle();

    if ($(this).text() === "Show Less") {
      $(this).text("Show More");
    } else {
      $(this).text("Show Less");
    }
  });
});

// ---------------- EXPERT PAGE FEATURES ----------------

// show more local experts
$("#show-more-local").click(function () {
  $(".extra-local").toggleClass("d-none");

  if ($(this).text() === "Show Less") {
    $(this).text("Show More");
  } else {
    $(this).text("Show Less");
  }
});

// show more global experts
$("#show-more-global").click(function () {
  $(".extra-global").toggleClass("d-none");

  if ($(this).text() === "Show Less") {
    $(this).text("Show More");
  } else {
    $(this).text("Show Less");
  }
});

// expert search
$("#expert-search").on("keyup", function () {
  let value = $(this).val().toLowerCase();

  $(".expert-card-wrapper").filter(function () {
    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
  });
});
