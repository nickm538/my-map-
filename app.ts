import { MapComponent } from './components/Map';
import { PinForm } from './components/PinForm';
import { SearchBar } from './components/SearchBar';
import { getCoordinates } from './services/geocoding';
import { addPin, getPins } from './services/pinService';

class App {
    private mapComponent: MapComponent;
    private pinForm: PinForm;
    private searchBar: SearchBar;

    constructor() {
        this.mapComponent = new MapComponent();
        this.pinForm = new PinForm(this.handlePinSubmit.bind(this));
        this.searchBar = new SearchBar(this.handleSearch.bind(this));
        
        this.initialize();
    }

    private initialize() {
        this.mapComponent.initMap();
        this.pinForm.render();
        this.searchBar.render();
        this.loadExistingPins();
    }

    private loadExistingPins() {
        const pins = getPins();
        pins.forEach(pin => this.mapComponent.addPin(pin));
    }

    private async handlePinSubmit(address: string) {
        const coordinates = await getCoordinates(address);
        if (coordinates) {
            const pin = { address, ...coordinates };
            addPin(pin);
            this.mapComponent.addPin(pin);
        }
    }

    private handleSearch(query: string) {
        this.mapComponent.searchLocation(query);
    }
}

const app = new App();