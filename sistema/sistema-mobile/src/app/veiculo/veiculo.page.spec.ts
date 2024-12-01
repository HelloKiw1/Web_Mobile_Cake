import { ComponentFixture, TestBed } from '@angular/core/testing';
import { veiculoPage } from './veiculo.page';

describe('veiculoPage', () => {
  let component: veiculoPage;
  let fixture: ComponentFixture<veiculoPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(veiculoPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
