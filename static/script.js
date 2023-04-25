class ClickableSelect {
    constructor(originalSelect) {

        this.originalSelect = originalSelect;
        this.ClickableSelect = document.createElement("div");
        this.ClickableSelect.classList.add("select");

        this.originalSelect.querySelectorAll("option").forEach((optionElement) => {
            const itemElement = document.createElement("div");

            itemElement.classList.add("select_item");
            itemElement.value = optionElement.value
            itemElement.textContent = optionElement.textContent;
            this.ClickableSelect.appendChild(itemElement);

            if (optionElement.selected) {
                this.select_item(itemElement);
            }

            itemElement.addEventListener("click", () => {             
                this.select_item(itemElement);
            });
        });

        this.originalSelect.insertAdjacentElement("afterend", this.ClickableSelect);
    }

    select_item(itemElement) {
        const index = Array.from(this.ClickableSelect.children).indexOf(itemElement);

        this.ClickableSelect.querySelectorAll(".select_item").forEach((el) => {
            el.classList.remove("select_item-selected");
        });
        
        this.originalSelect.querySelectorAll("option")[index].selected = true;

        var currencies = document.getElementsByClassName('currency');
        for (var i = 0; i < currencies.length; i++) {
            currencies.item(i).value = itemElement.value;
        }
        itemElement.classList.add("select_item-selected");
    }

    deselect_item(itemElement) {
        const index = Array.from(this.ClickableSelect.children).indexOf(itemElement);
        this.originalSelect.querySelectorAll("option")[index].selected = false;
        itemElement.classList.remove("select_item-selected");
    }
}

document.querySelectorAll(".clickable-select").forEach((Element) => {
    new ClickableSelect(Element);
});