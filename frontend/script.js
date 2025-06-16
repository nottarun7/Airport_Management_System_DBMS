const API = "http://localhost:5000";

document.addEventListener("DOMContentLoaded", () => {
  setupCRUD("passenger", ["name", "passport", "nationality", "gender", "dob"]);
  setupCRUD("flight", ["number", "source", "dest", "dep", "arr"]);
  setupCRUD("ticket", ["pid", "fid", "seat", "class", "price"]);
  setupCRUD("baggage", ["pid", "weight", "tag"]);
});

function setupCRUD(entity, fields) {
  const list = document.getElementById(`${entity}-list`);
  const form = document.getElementById(`${entity}-form`);
  const idField = document.getElementById(`${entity[0]}id`);

  const renderList = async () => {
    const res = await fetch(`${API}/${entity}s`);
    const data = await res.json();
    list.innerHTML = "";
    data.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item.join(" | ");
      const [id] = item;

      const delBtn = document.createElement("button");
      delBtn.textContent = "Delete";
      delBtn.onclick = async () => {
        await fetch(`${API}/${entity}/${id}`, { method: "DELETE" });
        renderList();
      };

      const updateBtn = document.createElement("button");
      updateBtn.textContent = "Update";
      updateBtn.classList.add("update");
      updateBtn.onclick = () => {
        idField.value = id;
        fields.forEach((f, i) => {
          document.getElementById(`${entity[0]}${f}`).value = item[i + 1];
        });
      };

      li.appendChild(updateBtn);
      li.appendChild(delBtn);
      list.appendChild(li);
    });
  };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = {};
    fields.forEach(f => {
      payload[f] = document.getElementById(`${entity[0]}${f}`).value;
    });

    const id = idField.value;
    if (id) {
      await fetch(`${API}/${entity}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
    } else {
      await fetch(`${API}/${entity}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
    }

    form.reset();
    renderList();
  });

  renderList();
}
